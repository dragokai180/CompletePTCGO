from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='20684e47-f0d0-543a-b4ce-83a8465ee351',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name',
    display_name='Bronzong',
    searchable_by=['Bronzong', 'Stage 1', 'Bronzong'],
    subtypes=['Stage 1'],
    collector_number=96,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name',
    family_id=436,
    abilities=[
        Attack(
            title='Pain Amplifier',
            game_text="Put 3 damage counters on each of your opponent's Pokémon that has any damage counters on it.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Knock Away',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
