from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a4ce74b2-5f4c-587e-8558-18ed6ef56ba7',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dugtrio.Name',
    display_name='Dugtrio',
    searchable_by=['Dugtrio', 'Stage 1', 'Dugtrio'],
    subtypes=['Stage 1'],
    collector_number=56,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name',
    family_id=50,
    abilities=[
        Attack(
            title='Slash',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title='Earthquake',
            game_text="This attack does 20 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
