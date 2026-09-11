from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fe6ce981-00ab-5a2d-91ec-725ee9027c65',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name',
    display_name='Grimer',
    searchable_by=['Grimer', 'Basic', 'Grimer'],
    subtypes=['Basic'],
    collector_number=126,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=88,
    abilities=[
        Attack(
            title='Super Poison Breath',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
