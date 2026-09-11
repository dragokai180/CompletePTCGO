from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9f5fffa2-58a3-5ba1-ad49-fa3dca9003f1',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name',
    display_name='Golbat',
    searchable_by=['Golbat', 'Stage 1', 'Golbat'],
    subtypes=['Stage 1'],
    collector_number=55,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name',
    family_id=41,
    abilities=[
        Attack(
            title='Super Poison Breath',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Acrobatics',
            game_text='Flip 2 coins. This attack does 20 more damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
