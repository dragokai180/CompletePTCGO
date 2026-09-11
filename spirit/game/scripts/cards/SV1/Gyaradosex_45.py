from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='fe5f5b67-d9e8-54c0-93bc-8890de14a6ff',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gyaradosex.Name',
    display_name='Gyarados ex',
    searchable_by=['Gyarados ex', 'Stage 1', 'Tera', 'ex', 'Gyaradosex'],
    subtypes=['Stage 1', 'Tera', 'ex'],
    collector_number=45,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name',
    family_id=129,
    abilities=[
        Attack(
            title='Waterfall',
            cost={PokemonTypes.WATER: 3},
            damage=100,
        ),
        Attack(
            title='Tyrannical Tail',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 180 more damage.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=180,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
