from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='529424be-adaa-5f96-9790-8c47bf12ee0e',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name',
    display_name='Bellsprout',
    searchable_by=['Bellsprout', 'Basic', 'Bellsprout'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=69,
    abilities=[
        Attack(
            title='Blot',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
