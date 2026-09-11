from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="c21e83eb-e950-58b8-b890-6ef6993d58c5",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsCorvisquire.Name",
    display_name="Hop's Corvisquire",
    searchable_by=["Hop's Corvisquire", "Stage 1", "HopsCorvisquire"],
    subtypes=["Stage 1"],
    collector_number=134,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsRookidee.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Speed Dive",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
