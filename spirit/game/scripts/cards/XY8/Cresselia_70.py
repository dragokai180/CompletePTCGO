from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='12877f47-dc00-5c4c-80cf-28366611c6ce',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name',
    display_name='Cresselia',
    searchable_by=['Cresselia', 'Basic', 'Cresselia'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=488,
    abilities=[
        Ability(
            title='My Way',
            game_text='If there is any Stadium card in play, this Pokémon has no Retreat Cost.',
            passive=standard_passive('If there is any Stadium card in play, this Pokémon has no Retreat Cost.'),
        ),
        Attack(
            title='Moonlight Gain',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
