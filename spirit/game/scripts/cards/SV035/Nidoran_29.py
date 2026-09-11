from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7777438e-a1f2-5225-af7f-0c88285d8d0c',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    display_name='Nidoran ♀',
    searchable_by=['Nidoran ♀', 'Basic', 'Nidoran'],
    subtypes=['Basic'],
    collector_number=29,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=29,
    abilities=[
        Attack(
            title='Poison Horn',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
