from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='074ee3b5-8d13-501c-a379-0fde07c1c1b1',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscruelex.Name',
    display_name='Toedscruel ex',
    searchable_by=['Toedscruel ex', 'Stage 1', 'ex', 'Toedscruelex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=22,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name',
    family_id=948,
    abilities=[
        Ability(
            title='Protective Mycelium',
            game_text="Prevent all effects of attacks used by your opponent's Pokémon done to all of your Pokémon that have Energy attached. (Existing effects are not removed. Damage is not an effect.)",
            passive=standard_passive("Prevent all effects of attacks used by your opponent's Pokémon done to all of your Pokémon that have Energy attached. (Existing effects are not removed. Damage is not an effect.)"),
        ),
        Attack(
            title='Colony Rush',
            game_text='This attack does 40 more damage for each of your Benched Pokémon that has any Grass Energy attached.',
            cost={PokemonTypes.GRASS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
