from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="54694224-b0b3-5a18-8f49-74444c7637d9",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDugtrio.Name",
    display_name="Team Rocket's Dugtrio",
    searchable_by=["Team Rocket's Dugtrio", "Stage 1", "TeamRocketsDugtrio"],
    subtypes=["Stage 1"],
    collector_number=101,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsDiglett.Name",
    family_id=50,
    abilities=[
        Ability(
            title="Holes",
            game_text="Whenever your opponent's Active Pokémon moves to the Bench during their turn, place 2 damage counters on that Pokémon.",
            passive=standard_passive("Whenever your opponent's Active Pokémon moves to the Bench during their turn, place 2 damage counters on that Pokémon."),
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
