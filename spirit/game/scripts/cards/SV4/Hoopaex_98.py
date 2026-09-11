from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid='5c232300-654b-53f9-9d27-9b5166efcf49',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoopaex.Name',
    display_name='Hoopa ex',
    searchable_by=['Hoopa ex', 'Basic', 'Tera', 'ex', 'Hoopaex'],
    subtypes=['Basic', 'Tera', 'ex'],
    collector_number=98,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=720,
    abilities=[
        Attack(
            title='Energy Crush',
            game_text="This attack does 50 damage for each Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title="Bandit's Fist",
            game_text="During your next turn, this Pokémon can't use Bandit's Fist.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=200,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
    passive=TeraRulePassive(),
)
