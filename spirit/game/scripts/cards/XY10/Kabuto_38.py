from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='000ce88b-2da3-5fda-a797-1af27368fd2c',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name',
    display_name='Kabuto',
    searchable_by=['Kabuto', 'Restored', 'Kabuto'],
    subtypes=['Restored'],
    collector_number=38,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.RESTORED,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.DomeFossilKabuto.Name',
    family_id=140,
    abilities=[
        Attack(
            title='Mud Shot',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
    ],
)
