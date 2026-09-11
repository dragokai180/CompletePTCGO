from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='36ca7d0e-dcfa-5170-8ec4-a9915ad4cbc7',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Armarougeex.Name',
    display_name='Armarouge ex',
    searchable_by=['Armarouge ex', 'Stage 1', 'ex', 'Armarougeex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=27,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name',
    family_id=935,
    abilities=[
        Ability(
            title='Crimson Armor',
            game_text="If this Pokémon has full HP, it takes 80 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).",
            passive=standard_passive("If this Pokémon has full HP, it takes 80 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Scorching Bazooka',
            game_text='This attack does 40 more damage for each Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
