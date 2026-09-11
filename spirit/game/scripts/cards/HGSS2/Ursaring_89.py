from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='86f39069-e198-5691-9cad-c5b2f204f820',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name',
    display_name='Ursaring',
    searchable_by=['Ursaring', 'Stage 1', 'Prime', 'Ursaring'],
    subtypes=['Stage 1', 'Prime'],
    collector_number=89,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name',
    family_id=216,
    abilities=[
        Ability(
            title='Berserk',
            game_text="If Ursaring has any damage counters on it, each of Ursaring's attacks does 60 more damage (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("If Ursaring has any damage counters on it, each of Ursaring's attacks does 60 more damage (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Hammer Arm',
            game_text="Discard the top card from your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Megaton Lariat',
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
        ),
    ],
)
