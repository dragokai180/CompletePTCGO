from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import AttrID, AbilityTypes, Rarities


def _salvatore_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck is not None and deck.children
                and board.pokemon_in_play(player_id))


def _eligible_evolution(card, previous_name):
    if card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) != previous_name:
        return False
    definition = def_for(card.archetype_id)
    return definition is not None and not any(
        ability.ability_type == AbilityTypes.POKE_ABILITY
        for ability in getattr(definition, "abilities", ())
    )


async def salvatore(ctx):
    # This effect evolves directly from the deck, including on the first turn
    # and on the turn the target entered play.
    targets = [pokemon for pokemon in ctx.my_pokemon_in_play()
               if pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)]
    target = await ctx.choose_pokemon(targets, "Choose a Pokémon to evolve") \
        if targets else None
    if target is None:
        return
    previous_name = target.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    picks = await ctx.search_deck(
        lambda card: _eligible_evolution(card, previous_name),
        count=1, minimum=0,
        prompt="Choose an Evolution Pokémon without an Ability",
    )
    if picks:
        await ctx.evolve_pokemon(target, picks[0])
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="08853f0b-d6af-56c8-bd9e-a5406da851c9",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Salvatore.Name",
    display_name="Salvatore",
    searchable_by=["Salvatore", "Supporter", "Salvatore"],
    subtypes=["Supporter"],
    collector_number=160,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=salvatore,
    condition=_salvatore_condition,
)
