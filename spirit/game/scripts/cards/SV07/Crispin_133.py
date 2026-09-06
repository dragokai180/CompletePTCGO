from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, Rarities, CLIENT_POKEMON_TYPE_NAMES, PokemonTypes
from spirit.game.card_effects.trainers import is_basic_energy_card


def _energy_type(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return types[0] if types else None


async def crispin(ctx):
    """Search for up to 2 Basic Energy of different types; put 1 into your
    hand and attach the other to 1 of your Pokémon. Then shuffle."""
    deck_cards = list(ctx.deck())
    reps = []
    labels = {}
    seen = []
    for card in deck_cards:
        if not is_basic_energy_card(card):
            continue
        energy_type = _energy_type(card)
        if energy_type is None or energy_type in seen:
            continue
        seen.append(energy_type)
        reps.append(card)
        type_name = CLIENT_POKEMON_TYPE_NAMES.get(
            PokemonTypes(energy_type), "Energy"
        )
        labels[card.entity_id] = f"{type_name} Energy"

    if not reps:
        await ctx.search_deck(
            is_basic_energy_card, count=2, minimum=0,
            prompt="Choose up to 2 Basic Energy cards of different types.",
        )
        await ctx.shuffle_deck()
        return

    picks = await ctx.choose_cards(
        reps, 2, minimum=0,
        prompt="Choose up to 2 Basic Energy cards of different types.",
        display_cards=deck_cards,
    )
    if not picks:
        await ctx.shuffle_deck()
        return

    if len(picks) == 1:
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
        return

    hand_pick = await ctx.choose_cards(
        picks, 1,
        prompt="Choose 1 Energy to put into your hand.",
    )
    if not hand_pick:
        await ctx.shuffle_deck()
        return
    to_hand = hand_pick[0]
    to_attach = next(c for c in picks if c is not to_hand)
    await ctx.put_in_hand([to_hand], reveal=True)
    targets = ctx.my_pokemon_in_play()
    if targets:
        label = labels.get(to_attach.entity_id, "Energy")
        target = await ctx.choose_pokemon(
            targets, f"Choose a Pokémon to attach {label} to"
        )
        if target is not None:
            await ctx.attach_energy(to_attach, target)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="f4f5b093-ea2b-5a3a-9176-ae2646dd9e53",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Crispin.Name",
    display_name="Crispin",
    searchable_by=["Crispin", "Supporter", "Crispin"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=crispin,
)
