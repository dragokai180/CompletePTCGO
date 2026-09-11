from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='84e9c8ba-ed45-5b99-becc-a08f23525930',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name',
    display_name='Tinkatuff',
    searchable_by=['Tinkatuff', 'Stage 1', 'Tinkatuff'],
    subtypes=['Stage 1'],
    collector_number=103,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name',
    family_id=957,
    abilities=[
        Attack(
            title='Light Punch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Boundless Power',
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
