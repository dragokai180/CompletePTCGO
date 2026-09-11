from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3e47f482-29a2-5306-b17a-aec16600f148',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name',
    display_name='Clefable',
    searchable_by=['Clefable', 'Stage 1', 'Clefable'],
    subtypes=['Stage 1'],
    collector_number=36,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name',
    family_id=35,
    abilities=[
        Attack(
            title='Follow Me',
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='More Moon',
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
