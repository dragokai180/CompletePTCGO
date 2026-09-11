from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5195c3a2-ae4c-57c4-9cb5-3af770586221',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name',
    display_name='Miltank',
    searchable_by=['Miltank', 'Basic', 'Miltank'],
    subtypes=['Basic'],
    collector_number=78,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=241,
    abilities=[
        Ability(
            title='Moomoo Malt',
            game_text='As long as this Pokémon is your Active Pokémon, whenever you attach an Energy card from your hand to 1 of your Pokémon, heal 90 damage from that Pokémon.',
            passive=standard_passive('As long as this Pokémon is your Active Pokémon, whenever you attach an Energy card from your hand to 1 of your Pokémon, heal 90 damage from that Pokémon.'),
        ),
        Attack(
            title='Sitdown Splash',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
