from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="8188a463-b115-5a17-90bb-2163c22d9210",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eternatus.Name",
    display_name="Eternatus",
    searchable_by=["Eternatus", "Basic", "Eternatus"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=890,
    abilities=[
        Attack(
            title="Dyna-Blast",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="World Ender",
            game_text="Discard a Stadium in play. If you can't, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.DARKNESS: 2},
            damage=230,
            effect=standard_attack,
        ),
    ],
)
