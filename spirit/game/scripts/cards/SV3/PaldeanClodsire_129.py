from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1fce15e9-669d-50ee-bf7d-9c51a35b1941',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsire.Name',
    display_name='Paldean Clodsire',
    searchable_by=['Paldean Clodsire', 'Stage 1', 'PaldeanClodsire'],
    subtypes=['Stage 1'],
    collector_number=129,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name',
    family_id=194,
    abilities=[
        Attack(
            title='Splattering Poison',
            game_text='Both Active Pokémon are now Poisoned.',
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Venoshock',
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
