from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a3e9afd1-d0be-53a3-b231-d337eb4781fa',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name',
    display_name='Absol',
    searchable_by=['Absol', 'Basic', 'Prime', 'Absol'],
    subtypes=['Basic', 'Prime'],
    collector_number=91,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.RarePrime,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=359,
    abilities=[
        Ability(
            title='Eye of Disaster',
            game_text='As long as Absol is your Active Pokémon, whenever your opponent puts a Basic Pokémon from his or her hand onto his or her Bench, put 2 damage counters on that Pokémon.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('As long as Absol is your Active Pokémon, whenever your opponent puts a Basic Pokémon from his or her hand onto his or her Bench, put 2 damage counters on that Pokémon.'),
        ),
        Attack(
            title='Vicious Claw',
            game_text="Choose 1 Pokémon from your hand and put it in the Lost Zone. (If you can't put a Pokémon in the Lost Zone, this attack does nothing.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
