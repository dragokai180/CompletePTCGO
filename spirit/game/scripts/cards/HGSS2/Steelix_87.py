from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fc35f2f8-2883-581d-9151-d1b2ed587b24',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name',
    display_name='Steelix',
    searchable_by=['Steelix', 'Stage 1', 'Prime', 'Steelix'],
    subtypes=['Stage 1', 'Prime'],
    collector_number=87,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name',
    family_id=95,
    abilities=[
        Ability(
            title='Perfect Metal',
            game_text="Steelix can't be affected by any Special Conditions",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("Steelix can't be affected by any Special Conditions"),
        ),
        Attack(
            title='Energy Stream',
            game_text='Search your discard pile for an Energy card and attach it to Steelix.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Gaia Crush',
            game_text='You may discard any Stadium card in play.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
