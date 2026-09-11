from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='95480d40-7a87-5e2d-a2fe-e0649b3f2fe2',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name',
    display_name='Abomasnow',
    searchable_by=['Abomasnow', 'Stage 1', 'Abomasnow'],
    subtypes=['Stage 1'],
    collector_number=42,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name',
    family_id=459,
    abilities=[
        Attack(
            title='Quick Freeze',
            game_text="If your opponent's Active Pokémon has any Water Energy attached to it, it is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title='Wild Tackle',
            game_text='This Pokémon does 20 damage to itself.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
