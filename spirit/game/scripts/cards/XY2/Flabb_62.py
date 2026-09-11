from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb75c4bc-6b1b-5ec9-ba97-570aac667f95',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name',
    display_name='Flabébé',
    searchable_by=['Flabébé', 'Basic', 'Flabb'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=669,
    abilities=[
        Attack(
            title='Aromatherapy',
            game_text='Heal 10 damage from each of your Pokémon.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
    ],
)
