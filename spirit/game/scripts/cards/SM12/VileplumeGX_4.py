from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e0a2ed45-1ce2-52e2-9e39-feae3904edde',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.VileplumeGX.Name',
    display_name='Vileplume-GX',
    searchable_by=['Vileplume-GX', 'Stage 2', 'GX', 'VileplumeGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=4,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    family_id=43,
    abilities=[
        Ability(
            title='Fragrant Flower Garden',
            game_text='Once during your turn (before your attack), you may heal 30 damage from each of your Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Massive Bloom',
            game_text='This attack does 10 less damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=180,
            damage_operator='-',
            effect=standard_attack,
        ),
        Attack(
            title='Allergic Explosion-GX',
            game_text="Your opponent's Active Pokémon is now Burned, Paralyzed, and Poisoned. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
