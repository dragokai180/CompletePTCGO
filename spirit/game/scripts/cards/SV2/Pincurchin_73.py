from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='987577b5-4366-5d2a-b89c-eb1e03de2186',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pincurchin.Name',
    display_name='Pincurchin',
    searchable_by=['Pincurchin', 'Basic', 'Pincurchin'],
    subtypes=['Basic'],
    collector_number=73,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=871,
    abilities=[
        Attack(
            title='Stun Needle',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Follow-Up Kerzap',
            game_text='You can use this attack only if this Pokémon used Stun Needle during your last turn.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
