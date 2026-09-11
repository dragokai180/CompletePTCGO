from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b6a0d76e-7f36-58ab-8405-f2de7821666e',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name',
    display_name='Rhyhorn',
    searchable_by=['Rhyhorn', 'Basic', 'Rhyhorn'],
    subtypes=['Basic'],
    collector_number=92,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=111,
    abilities=[
        Attack(
            title='Push Down',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
