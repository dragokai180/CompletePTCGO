from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ed79555b-d825-5b83-ae2c-7f79608ba8ae',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name',
    display_name='Yveltal',
    searchable_by=['Yveltal', 'Basic', 'Yveltal'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=717,
    abilities=[
        Attack(
            title='Strafe',
            game_text='You may switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Oblivion Wing',
            game_text='Attach a Darkness Energy card from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
