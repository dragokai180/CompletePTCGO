from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='804662a7-fd1d-51f1-bafe-061d90264d6a',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswine.Name',
    display_name='Mamoswine',
    searchable_by=['Mamoswine', 'Stage 2', 'Mamoswine'],
    subtypes=['Stage 2'],
    collector_number=21,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name',
    family_id=220,
    abilities=[
        Attack(
            title='Double Stomp',
            game_text='Flip 2 coins. This attack does 30 more damage for each heads.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Forceful Tackle',
            game_text='You may put up to 9 damage counters on this Pokémon. This attack does 10 more damage for each damage counter you placed in this way.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
