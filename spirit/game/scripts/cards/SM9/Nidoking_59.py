from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='af30bdb0-142d-5b3f-a4a1-339772faa9e1',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name',
    display_name='Nidoking',
    searchable_by=['Nidoking', 'Stage 2', 'Nidoking'],
    subtypes=['Stage 2'],
    collector_number=59,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorino.Name',
    family_id=32,
    abilities=[
        Attack(
            title='Drag Off',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. This attack does 50 damage to the new Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title="King's Drum",
            game_text='If Nidoqueen is on your Bench, this attack does 100 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
