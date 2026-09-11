from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0157e050-cf50-5675-bae5-12f19138613c',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name',
    display_name='Dunsparce',
    searchable_by=['Dunsparce', 'Basic', 'Dunsparce'],
    subtypes=['Basic'],
    collector_number=29,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=206,
    abilities=[
        Attack(
            title='Return',
            game_text='Draw cards until you have 6 cards in your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
