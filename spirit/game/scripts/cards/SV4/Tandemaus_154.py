from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9af887aa-272f-5687-9e4a-8585528f9bf0',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name',
    display_name='Tandemaus',
    searchable_by=['Tandemaus', 'Basic', 'Tandemaus'],
    subtypes=['Basic'],
    collector_number=154,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=924,
    abilities=[
        Attack(
            title='Tumble Over',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
