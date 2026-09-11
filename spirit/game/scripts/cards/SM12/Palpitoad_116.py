from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1fb698ea-0351-5b6b-b759-18ed1a2f3156',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Palpitoad.Name',
    display_name='Palpitoad',
    searchable_by=['Palpitoad', 'Stage 1', 'Palpitoad'],
    subtypes=['Stage 1'],
    collector_number=116,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name',
    family_id=535,
    abilities=[
        Attack(
            title='Mini Earthquake',
            game_text="This attack does 10 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
