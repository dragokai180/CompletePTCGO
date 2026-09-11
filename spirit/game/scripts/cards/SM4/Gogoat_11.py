from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3e940188-dae2-5a82-9e4a-ddb4baea2efb',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gogoat.Name',
    display_name='Gogoat',
    searchable_by=['Gogoat', 'Stage 1', 'Gogoat'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name',
    family_id=672,
    abilities=[
        Ability(
            title='Sap Sipper',
            game_text="This Pokémon's attacks do 80 more damage to your opponent's Grass Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("This Pokémon's attacks do 80 more damage to your opponent's Grass Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Horn Leech',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
