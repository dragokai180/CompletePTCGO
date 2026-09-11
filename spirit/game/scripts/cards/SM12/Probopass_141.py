from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6553090d-58f4-54ac-8867-8003e8a3ded8',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name',
    display_name='Probopass',
    searchable_by=['Probopass', 'Stage 1', 'Probopass'],
    subtypes=['Stage 1'],
    collector_number=141,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name',
    family_id=299,
    abilities=[
        Attack(
            title='Hard Press',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Triple Nose',
            game_text='Flip 3 coins. This attack does 40 more damage for each heads.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
