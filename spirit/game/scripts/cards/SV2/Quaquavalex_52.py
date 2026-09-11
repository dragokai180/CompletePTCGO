from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f25acc6-3912-5ed5-a178-ad106d10eae4',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quaquavalex.Name',
    display_name='Quaquaval ex',
    searchable_by=['Quaquaval ex', 'Stage 2', 'ex', 'Quaquavalex'],
    subtypes=['Stage 2', 'ex'],
    collector_number=52,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Quaxwell.Name',
    family_id=912,
    abilities=[
        Attack(
            title='Exciting Dance',
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. If you do, switch out your opponent's Active Pokémon to the Bench.\xa0(Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Spiral Shot',
            game_text='Put 2 Energy attached to this Pokémon into your hand.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=standard_attack,
        ),
    ],
)
