from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='822167f4-4b50-5f7a-a235-485d2da11875',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name',
    display_name='Hawlucha',
    searchable_by=['Hawlucha', 'Basic', 'Hawlucha'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=701,
    abilities=[
        Ability(
            title='Flying Entry',
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may choose 2 of your opponent's Benched Pokémon and put 1 damage counter on each of them.",
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Wing Attack',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
