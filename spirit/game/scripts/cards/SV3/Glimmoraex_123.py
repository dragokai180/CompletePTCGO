from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cff19746-31c7-5c21-a57b-686c613cef19',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Glimmoraex.Name',
    display_name='Glimmora ex',
    searchable_by=['Glimmora ex', 'Stage 1', 'ex', 'Glimmoraex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=123,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name',
    family_id=969,
    abilities=[
        Ability(
            title='Dust Field',
            game_text="As long as this Pokémon is in the Active Spot, your opponent can't have more than 3 Benched Pokémon. If they have 4 or more Benched Pokémon, they discard Benched Pokémon until they have 3 Pokémon on the Bench. If more than one effect changes the number of Benched Pokémon allowed, use the smaller number.",
            passive=standard_passive("As long as this Pokémon is in the Active Spot, your opponent can't have more than 3 Benched Pokémon. If they have 4 or more Benched Pokémon, they discard Benched Pokémon until they have 3 Pokémon on the Bench. If more than one effect changes the number of Benched Pokémon allowed, use the smaller number."),
        ),
        Attack(
            title='Poisonous Gem',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
