from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ba8af9a8-5ee3-5554-b158-20986424c333',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name',
    display_name='Beldum',
    searchable_by=['Beldum', 'Basic', 'Beldum'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=374,
    abilities=[
        Attack(
            title='Core Beam',
            game_text='Discard a Metal Energy from this Pokémon.',
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
