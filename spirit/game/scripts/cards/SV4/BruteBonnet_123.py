from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4989b2c7-22a8-513f-80fb-702e2581e3ea',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BruteBonnet.Name',
    display_name='Brute Bonnet',
    searchable_by=['Brute Bonnet', 'Basic', 'Ancient', 'BruteBonnet'],
    subtypes=['Basic', 'Ancient'],
    collector_number=123,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=986,
    abilities=[
        Ability(
            title='Toxic Powder',
            game_text='Once during your turn, if this Pokémon has an Ancient Booster Energy Capsule attached, you may make both Active Pokémon Poisoned.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Rampaging Hammer',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
