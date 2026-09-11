from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2b4fb12a-5ab5-5b89-a8ea-9a3648edca13',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name',
    display_name='Talonflame',
    searchable_by=['Talonflame', 'Stage 2', 'Talonflame'],
    subtypes=['Stage 2'],
    collector_number=30,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name',
    family_id=661,
    abilities=[
        Attack(
            title='Clutch',
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Fiery Breeze',
            game_text='If this Pokémon has any damage counters on it, this attack does 90 more damage.',
            cost={PokemonTypes.FIRE: 1},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
