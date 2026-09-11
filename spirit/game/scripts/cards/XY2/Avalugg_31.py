from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c52d956c-3779-5777-9ff8-c4a7b1f2c35f',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Avalugg.Name',
    display_name='Avalugg',
    searchable_by=['Avalugg', 'Stage 1', 'Avalugg'],
    subtypes=['Stage 1'],
    collector_number=31,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name',
    family_id=712,
    abilities=[
        Attack(
            title='Frost Barrier',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Shatter',
            game_text='Discard any Stadium card in play.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
