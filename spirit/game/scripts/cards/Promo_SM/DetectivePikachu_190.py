from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc3ef76e-bdb9-5012-99f4-81a30b359cb4',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.DetectivePikachu.Name',
    display_name='Detective Pikachu',
    searchable_by=['Detective Pikachu', 'Basic', 'DetectivePikachu'],
    subtypes=['Basic'],
    collector_number=190,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=25,
    abilities=[
        Attack(
            title='Coffee Break',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Corkscrew Punch',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
