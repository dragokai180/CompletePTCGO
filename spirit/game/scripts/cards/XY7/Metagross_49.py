from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ba0642e5-af29-5fb2-b815-7fd2d18df58f',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name',
    display_name='Metagross',
    searchable_by=['Metagross', 'Stage 2', 'Metagross'],
    subtypes=['Stage 2'],
    collector_number=49,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name',
    family_id=374,
    abilities=[
        Ability(
            title='Magnetic Warp',
            game_text='Once during your turn (before your attack), you may switch your Active Pokémon with 1 of your Benched Pokémon. If you do, your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Iron Cannon',
            game_text='You may discard all Metal Energy attached to this Pokémon. If you do, this attack does 80 more damage.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
