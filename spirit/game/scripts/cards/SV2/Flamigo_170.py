from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='697cd5b9-69da-544a-bf79-704bacd7425c',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flamigo.Name',
    display_name='Flamigo',
    searchable_by=['Flamigo', 'Basic', 'Flamigo'],
    subtypes=['Basic'],
    collector_number=170,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=973,
    abilities=[
        Ability(
            title='Insta-Flock',
            game_text='When you play this Pokémon from your hand onto your Bench during your turn, you may search your deck for up to 3 Flamigo, reveal them, and put them into your hand. Then, shuffle your deck.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='United Wings',
            game_text='This attack does 20 damage for each Pokémon in your discard pile that has the United Wings attack.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
