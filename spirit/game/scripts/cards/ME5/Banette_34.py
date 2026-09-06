from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import full_effect_shield_passive


async def puppet_pull(ctx):
    """80. You may search your deck for a card and put it into your hand."""
    await ctx.deal_damage()
    if not await ctx.ask_yes_no("Search your deck for a card and put it into your hand?"):
        return
    picks = await ctx.search_deck(
        count=1, minimum=0,
        prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="9fcac721-0e60-5dd8-925b-34eef2ce3fa5",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette","Stage 1","Banette"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    family_id=353,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    abilities=[
        Ability(
            title="Hide 'n' Sneak",
            game_text="Prevent all effects of your opponent's Pokémon's attacks and Abilities done to this Pokémon. (Damage is not an effect.)",
            passive=full_effect_shield_passive(),
        ),
        Attack(
            title="Puppet Pull",
            game_text="You may search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=80,
            effect=puppet_pull,
        ),
    ],
)
